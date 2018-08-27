FROM uribench/madness:1.0.0
COPY . .
ENTRYPOINT ["madness", "--theme=/_theme"]
