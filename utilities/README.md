##  make-qr-code.py

creates QR codes

### Installation and Usage
```
pipenv install
# usage: make-qr-code.py [-h] [--font FONT] url image output label
pipenv run python make-qr-code.py "https://app.sli.do/event/3PHAk58CkgG7vRTJzKLeA9/embed/polls/77380faa-861a-4e14-a740-81089a2d0d66" "../docs/images/trust_fez_icon.jpeg" "familiar-poll.png" "Familiarity Poll"
```

### Argument Descriptions
```
pipenv run python make-qr-code.py --help
```