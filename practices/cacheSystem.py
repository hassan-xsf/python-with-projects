# cache decorator, So if it's called again the cached value is returned instead of calculating it all again.
# Expiry option on cache
# Expire cache
# Revalidate cache.

import time

CACHE_EXPIRE_TIME = 60

def cacheResult(func):
    cache = {}
    def wrapper(*args , **kwargs):
        cache_key = (str(args) + str(kwargs.items()))

        currentTime = time.time()

        if cache_key in cache:
            cache_data = cache[cache_key]
            if(currentTime > cache_data["expiryTime"]):
                print("Cache expired")
                del cache[cache_key]
            else:
                print("Cache found!")
                return cache_data["result"]
                
        cache[cache_key] = {"result" : func(*args , **kwargs) , "expiryTime" : currentTime + CACHE_EXPIRE_TIME}

        print("Cache not found!")
        return cache[cache_key]["result"]

    def expireCache(*args , **kwargs):
        cache_key = str(args) + str(kwargs.items())
        if not cache_key in cache:
            print("No cache found to expire")
        else:
            del cache[cache_key]
            print("Cache deleted")

    def revalidateCache(*args , **kwargs):
        cache_key = str(args) + str(kwargs.items())
        cache[cache_key] = {"result" : func(*args , **kwargs) , "expiryTime" : time.time() + CACHE_EXPIRE_TIME}
        print("Cache revalidated succesfully")
    
    wrapper.revalidateCache = revalidateCache

    wrapper.expireCache = expireCache
    return wrapper


users = [
    {"id" : 0 , "name" : "Hassan"},
    {"id" : 1 , "name" : "Areeba"},
    {"id" : 2 , "name" : "Saad"},
]

@cacheResult
def getUser(id):
    for user in users:
        if user["id"] == id:
            return f"ID: {user["id"]} | NAME: {user["name"]}"
    return "Not found"

print(getUser(1))

users[1]["name"] = "Salma" # Since we changed the name, We need to revalidaate the cache or expire.
getUser.revalidateCache(1)
# getUser.expireCache(1)

print(getUser(1))





