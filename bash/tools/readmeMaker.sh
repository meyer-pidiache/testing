#!/bin/bash

echo "\`\`\`" > README.md

tree --gitignore >> README.md

echo "\`\`\`" >> README.md

echo "Done!"

