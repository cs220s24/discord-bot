cd ~/discord-bot
docker run --name redisdb --network=botdb -d -p 6379:6379 -v $(pwd)/data:/data redis
docker run -it --name discord-bot --network=botdb discord-bot
