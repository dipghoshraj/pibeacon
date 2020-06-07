# Pibeacon
Pibeacon is a project for run and scanning ibeacon and eddystone beacons in raspberry pi

## Run beacon simulation
To run ibeaconn simulation go to cloned folder and run follwoing command

```bash
sh broadcasting/ibeacon.sh
```

To run eddystone simulation go to cloned folder and run follwoing command

```bash 
sh broadcasting/eddystone.sh
```

## Run beacon scanner 
To install all dependencies for scanner 

```bash
npm build
```
```bash
npm install
```

To run scanner go to scanner folder
```bash 
node app.js
```


