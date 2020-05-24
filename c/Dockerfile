FROM gcc:4.9 AS builder
WORKDIR /ctf
COPY TimeRNG.cpp ./
RUN gcc -o timeRNG TimeRNG.cpp

FROM alpine/socat
COPY --from=builder /ctf .
COPY start.sh .
CMD ["bash start.sh"]
#CMD ["socat", "TCP-LISTEN:23232,reuseaddr,fork EXEC:./timeRNG"]
