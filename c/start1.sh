#!/bin/sh -e
socat TCP-LISTEN:23232,reuseaddr,fork EXEC:"./stack0" &
socat TCP-LISTEN:23233,reuseaddr,fork EXEC:"./stack1" &
socat TCP-LISTEN:23234,reuseaddr,fork EXEC:"./stack2" &
socat TCP-LISTEN:23235,reuseaddr,fork EXEC:"./Time" &
