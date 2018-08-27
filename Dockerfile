FROM uribench/madness:1.0.2
COPY . .
ENTRYPOINT ["madness", "--theme=/_theme"]
