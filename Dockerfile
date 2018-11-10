FROM uribench/madness:1.0.3

ENV PORT 3000

COPY . .
COPY entrypoint /bin/entrypoint

RUN chmod +x /bin/entrypoint

ENTRYPOINT ["bash"]
CMD ["/bin/entrypoint"]
