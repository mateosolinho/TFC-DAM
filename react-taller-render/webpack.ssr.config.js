const path = require('path');
const nodeExternals = require('webpack-node-externals');

module.exports = {
    mode: 'production',
    entry: path.resolve('src', 'ssr.js'),
    output: {
        filename: 'ssr.js',
        libraryTarget: 'commonjs2',
    },

    target: 'node',
    externals: nodeExternals(),

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-react']
                    },
                },

                exclude: /node_modules/,
            },
        ],
    },

    resolve: {
        extensions: ['.jsx', '.js']
    }
}