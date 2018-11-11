FROM uribench/madness:1.0.3

COPY . .

ENTRYPOINT ["bash", "-c"]
CMD ["madness --theme /_theme --port ${PORT:-3000}"]
