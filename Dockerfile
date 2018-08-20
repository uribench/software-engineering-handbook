FROM uribench/madness
COPY . .
ENTRYPOINT ["madness", "--theme=/_theme"]
