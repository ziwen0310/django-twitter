def invalidate_object_cache(sender, instance, **kwargs):
    from utils.memcashed_helper import MemcachedHelper
    MemcachedHelper.invalidate_cached_object(sender, instance.id)