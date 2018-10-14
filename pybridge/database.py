import logging

from sqlalchemy.orm.exc import NoResultFound


def get_one_or_create_feedback(session,
                      model,
                      create_method='',
                      create_method_kwargs=None,
                      **kwargs):
    try:
        kwargslist = []
        kwargscalars = {}
        for k in kwargs:
            if isinstance(kwargs[k], list):
                kwargslist += [getattr(model, k).contains(x) for x in kwargs[k]]
            else:
                kwargscalars[k] = kwargs[k]
        return True,session.query(model).filter_by(**kwargscalars).filter(and_(*kwargslist)).one()
    except NoResultFound:
        try:
            from sqlalchemy.inspection import inspect
            id = {key.name:kwargs[key.name] for key in inspect(model).primary_key if key.name in kwargs}
            if len(id) == len(inspect(model).primary_key):
                fetched = session.query(model).filter_by(**id).first()
                if fetched is not None:
                    for key in kwargs:
                        setattr(fetched,key,kwargs[key])
                    session.commit()
                    return True,fetched
            kwargs.update(create_method_kwargs or {})
            created = getattr(model, create_method, model)(**kwargs)

            session.add(created)
            session.commit()
            return False,created
        except Exception as ex:
            logging.debug(
                string_concat('get one or create Rolling back session ', session, ' for model ', model, ' kwargs', kwargs,' exception',ex))
            session.rollback()
        finally:
            pass
    finally:
        pass


def get_one_or_create(session,
                      model,
                      create_method='',
                      create_method_kwargs=None,
                      **kwargs):
    try:
        retrieved,obj = get_one_or_create_feedback(session,model,create_method=create_method,create_method_kwargs=create_method_kwargs,**kwargs)
        return obj
    except TypeError:
        obj = get_one_or_create_feedback(session, model, create_method=create_method,
                                                    create_method_kwargs=create_method_kwargs, **kwargs)
        return obj
