# Serial Monitor Cli

As the maintainer of this project, please make a few updates:

- Updating SUPPORT.MD with content about this project's support experience
- Understanding the security reporting process in SECURITY.MD
- Remove this section from the README

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

### Setting Up Dev Environment

- Create Python 3.8 Virtual Environment
	```cmd
	python -m venv ./.venv
	```
- Activate environment and install dependecies
	```cmd
	.venv\Script\Activate
	pip install -r requirements.txt
	```

### Dev Dependecies

- A device that can connect to a serial port (e.g. Arduino Uno)
- Sample Arduino Code for test device:
    ```C++
    int i = 0;

    void setup() {
        Serial.begin(9600);
    }

    void loop() {
        Serial.println(i);
        i++;
        delay(1000);
    }
    ```
### Setting up the debugger

1. Connect your test device to you computer
1. Run `python main.py --list-ports` to find which port your device is connected to
1. Open `launch.json` in `.vscode`
1. Edit args to match the current port: 
    > "args": ["open", "{your-port-here}", "-b 9600"]
1. Press F5 to start debugging

### Building the Code
```cmd
pyinstaller .\src\main.py --onefile
```

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
