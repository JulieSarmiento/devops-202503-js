#!/bin/bash

read -p "What's your name? " name
read -p "what's your age? " age

if [[ $name && $age -gt 21 ]]; then
  echo "Hello, $name! You are $age years old, you are rich!"
else
  echo "Hello, $name! You are $age years old, you are a baby, so no money!"
fi

