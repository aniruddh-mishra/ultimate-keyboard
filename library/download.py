from gutenbergpy.gutenbergcache import GutenbergCache
#for sqlite

cache  = GutenbergCache.get_cache()
print(cache.native_query("SELECT * FROM books"))
