<div align="center">
  
```
          _______  _______  _        _______  _______  _______  _______         _ 
|\     /|(  ____ \(  ___  )| \    /\(  ____ )(  ___  )(  ____ \(  ____ \       / )
| )   ( || (    \/| (   ) ||  \  / /| (    )|| (   ) || (    \/| (    \/   _  / / 
| | _ | || (__    | (___) ||  (_/ / | (____)|| (___) || (_____ | (_____   (_)( (  
| |( )| ||  __)   |  ___  ||   _ (  |  _____)|  ___  |(_____  )(_____  )     | |  
| || || || (      | (   ) ||  ( \ \ | (      | (   ) |      ) |      ) |   _ ( (  
| () () || (____/\| )   ( ||  /  \ \| )      | )   ( |/\____) |/\____) |  (_) \ \ 
(_______)(_______/|/     \||_/    \/|/       |/     \|\_______)\_______)       \_)
```    
</div>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/sunw4r/weakpass?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/sunw4r/weakpass?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/sunw4r/weakpass?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/sunw4r/weakpass?color=56BEB8">
</p>

## ##

`weakpass` is a basic script that automates the generation of weak and standardized passwords. Designed to be a simple but valuable tool during the initial phase of security tests.

## Installation ##

go install github.com/phor3nsic/weakpass@latest

## Usage ##

To get a list of options:
```
weakpass -h
```

Example for a small list focused on a web spraying attack:
```
weakpass -c microsoft -w
```

Example for a big list focused on brute force cracking (eg: hashcat):
```
weakpass -c microsoft -b -o mscrack.txt 
```

Example for multi companies:
```
weakpass -c microsoft,xbox,skype -b -o mscrack.txt 
```

<div align="center">
<img src="https://raw.githubusercontent.com/sunw4r/assets/master/weakpass_sample.png"/>
</div>
