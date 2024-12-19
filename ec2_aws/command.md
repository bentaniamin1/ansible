1) Install module boto3 in python, permit connection between ansible (controle node) and aws
2) ansible-galaxy role init <name role>
3) ansible-vault encrypt_string --vault-password-file files/password 'key' --name 'aws_secret_key'
4) encrypting file existing -> ansible-vault encrypt main.yml --vault-password-file ../files/password
5) ansible localhost -m ansible.builtin.debug -a var="aws_secret_key" -e "@main.yml" --vault-pass
word-file ../files/password
6) ansible-vault rekey