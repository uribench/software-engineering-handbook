FROM uribench/madness:1.0.3
COPY . .
ENTRYPOINT ["madness", "--theme=/_theme"]
