FROM uribench/madness

COPY . .

ENTRYPOINT ["bash", "-c"]
CMD ["madness --theme /_theme --port ${PORT:-3000}"]
