#1 - In this Subnet?
Determine if given ip-address in a given subnet.
Solution implemented in python with 3 classes:
1. hexConvert --> converts given 32-bit unsigned int value to long and its ip-address
2. subnetRange --> given ip&subnet in CIDR format, determines its range, network ip, broadcast ip etc.
3. isThisSubnet --> verifies if ip is in subnet or not
Tests for each class provided in tests.py
--Provide a CLI interface: main.py
```python main.py addressSubnetPairs.csv output.csv```

#2 - Change of Phone Number
Solution provided in changeOfPhoneNumber.sh script, single command using SED - stream editor
Tested locally using similar script, test.sh with samples provided in var.zip

#3 - Implement an LRU Cache - 

Run on an f1-micro (1 vCPU, 0.6 GB memory) - GCP
Ensure port 38080 is opened

```sudo yum -y install git```

```git clone https://github.com/s3p02/amsrehwa.git```

```cd amsrehwa/problem3```

```bash prep.sh```

```source py36env/bin/activate```

```pip install -r requirements.txt ```

```vim app.py```
change instanceIp='' to instanceIp='YOUR_IP_ADDRESS'

```sudo mkdir -p /var/log/problem3```

```chmod -R 0777 /var/log/problem3``` chmod -->  as SU


```touch /var/log/problem3/output.log```


```chmod 644 /var/log/problem3/output.log```


```nohup python app.py > /var/log/problem3/output.log &```

```curl "http://YOUR_IP_ADDRESS:38080/example-route?lat=90&lng=180"``` from the terminal