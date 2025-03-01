const path = require('path');

module.exports = {
    entry: {
        vendor: ['@babel/polyfill', 'react'],
        app: ['./src/index.js']
    },

    output: {
        path: path.resolve(__dirname, 'public'),
        filename: '[name].js'
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                },

                exclude: /node_modules/
            }
        ],
    },

    resolve: {
        extensions: ['.js', '.jsx']
    }
}