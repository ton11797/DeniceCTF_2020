#!/bin/sh -e
socat TCP-LISTEN:23232,reuseaddr,fork EXEC:./timeRNG