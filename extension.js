const vscode = require('vscode');
const path = require('path');
const fs = require('fs');

function activate(context) {
    console.log('ArrowPrint extension is now active!');

    // Применяем цвета сразу при активации
    applySyntaxColors();

    // Команда запуска кода (треугольник)
    let runCommand = vscode.commands.registerCommand('arrowprint.runCode', function () {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active editor found');
            return;
        }

        const document = editor.document;
        const filePath = document.fileName;
        
        // Путь к вашему интерпретатору
        const interpreterPath = path.join(__dirname, 'interpreter.py');
        
        // Проверяем, существует ли файл интерпретатора
        if (!fs.existsSync(interpreterPath)) {
            vscode.window.showErrorMessage(
                `Interpreter not found! Please place interpreter.py in: ${__dirname}`
            );
            return;
        }

        // Создаем терминал
        let terminal = vscode.window.terminals.find(t => t.name === 'ArrowPrint');
        if (!terminal) {
            terminal = vscode.window.createTerminal('ArrowPrint');
        }
        terminal.show();

        // Запускаем ТОЛЬКО интерпретатор
        terminal.sendText(`python "${interpreterPath}" "${filePath}"`);
    });

    context.subscriptions.push(runCommand);

    vscode.window.showInformationMessage('ArrowPrint extension activated! 🎯');
}

function applySyntaxColors() {
    const config = vscode.window.terminals.find(t => t.name === 'ArrowPrint');
    if (!config) return;
    
    const colorCustomizations = {
        "textMateRules": [
            {
                "scope": "comment.line.arrowprint",
                "settings": { "foreground": "#6A9955", "fontStyle": "italic" }
            },
            {
                "scope": "string.quoted.double.arrowprint",
                "settings": { "foreground": "#CE9178" }
            },
            {
                "scope": "constant.numeric.arrowprint",
                "settings": { "foreground": "#B5CEA8" }
            },
            {
                "scope": "keyword.direction.arrowprint",
                "settings": { "foreground": "#569CD6", "fontStyle": "bold" }
            },
            {
                "scope": "keyword.stack.arrowprint",
                "settings": { "foreground": "#D7BA7D" }
            },
            {
                "scope": "keyword.math.arrowprint",
                "settings": { "foreground": "#C586C0" }
            },
            {
                "scope": "keyword.conditional.arrowprint",
                "settings": { "foreground": "#FFD700" }
            },
            {
                "scope": "keyword.compare.arrowprint",
                "settings": { "foreground": "#9CDCFE" }
            },
            {
                "scope": "keyword.array.arrowprint",
                "settings": { "foreground": "#4EC9B0" }
            },
            {
                "scope": "keyword.contain.arrowprint",
                "settings": { "foreground": "#CE9178" }
            },
            {
                "scope": "keyword.input.arrowprint",
                "settings": { "foreground": "#FF6B6B" }
            },
            {
                "scope": "keyword.stop.arrowprint",
                "settings": { "foreground": "#FF0000", "fontStyle": "bold underline" }
            }
        ]
    };

    try {
        const config = vscode.workspace.getConfiguration();
        config.update('editor.tokenColorCustomizations', colorCustomizations, vscode.ConfigurationTarget.Global);
    } catch (error) {
        console.error('Error applying colors:', error);
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};