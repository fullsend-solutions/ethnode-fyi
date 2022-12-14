geth-fyi
=============================

[geth.fyi](https://geth.fyi) provides live console output of the [geth](https://geth.ethereum.org/) 
and [prysm](https://prysmaticlabs.com/) Ethereum clients. This [python script](node/main.py) runs on
a custom-built Windows machine to upload the console output to a Firebase Realtime Database. The geth and prysm console output is written to two separate text files. To [achieve this](https://stackoverflow.com/questions/796476/displaying-windows-command-prompt-output-and-redirecting-it-to-a-file),
in Command Prompt run the following command for geth:
```
geth --http --http.api eth,net,engine,admin --authrpc.jwtsecret C:\Users\richa\Downloads\ethereum\consensus\jwt.hex 1>a.txt 2>&1 | type a.txt
```
and the following command for prysm:
```
prysm.bat beacon-chain --execution-endpoint=http://localhost:8551 --jwt-secret=C:\Users\richa\Downloads\ethereum\consensus\jwt.hex --suggested-fee-recipient=0x65eea517faaC6c7c611Ebe32cA7f46De8E3a08F9 1>b.txt 2>&1 | type b.txt
```
The python script uses three threads. One each to read from the geth and prysm text files and a third to upload the lines
to Firebase. This way, the order at which lines are outputted to the console is preserved.

This project was built by Fullsend Solutions, a software studio based in Los Angeles helping innovative companies build best-in-class apps.
Building software? Reach out to [lets@fullsend.io](mailto:lets@fullsend.io).
