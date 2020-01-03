#!/bin/bash

echo "Expecting Dacncer in $DANCER_HOME"
TARGET=mumble.frubumi.de

if [ -n "$DANCER_HOME" ] && [ -d "$DANCER_HOME" ]; then
  echo "Building $DANCER_HOME"
  cd $DANCER_HOME || exit
  mvn package
  scp target/dancer-0.0.1-SNAPSHOT.jar root@$TARGET:/root
  ssh root@$TARGET << EOF
    killall -9 java
    nohup "java -jar /root/dancer-0.0.1-SNAPSHOT.jar > foo.out 2> foo.err < /dev/null"
EOF
else
  echo "dancer home does not point to a directory"
fi