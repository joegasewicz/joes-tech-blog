IMG_NAME=bandnoticeboard/nottoboard:joes-blog-web-0.0.1

docker-build-macos:
	docker build --no-cache --tag $(IMG_NAME) .

docker-build-linux:
	export DOCKER_DEFAULT_PLATFORM=linux/amd64 && docker build --no-cache --tag $(IMG_NAME) .

docker-run:
	docker run --env-file ../.env --rm -p 8000:8000 $(IMG_NAME)

docker-push:
	docker push $(IMG_NAME)

docker-remove:
	docker rmi $(IMG_NAME)

cc:
	docker exec -it $(IMG_NAME) bash

docker-prune:
	docker system prune --all

set-env-vars:
	export $(grep -v '^#' ../.env-dev | xargs)