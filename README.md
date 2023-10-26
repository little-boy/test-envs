## Docker examples

- To run : `docker run --rm -it $(docker build -q .)` : build & run, then automatically clear cache.
- Other way : 
    - `docker build -t my-build .` (tells Docker to build the current folder with any files found in it, with the tag `my-build`)
    - `docker run -it my-build` (tells Docker to run the previous image created)

### Notions :
- layer caching,
- ports,
  - opt `-p`
- bind mounts,
  - opt `--mount` (type bind)
- volume binding,
  - opt `--mount` (type volume)
