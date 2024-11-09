const path = require('path');
const webpack = require("webpack");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
// const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
    entry: './public/js/index.js',
    output: {
        path: path.resolve(__dirname, 'static'),
        filename: "[name].bundle.js",
    },
    mode: "development",
    module: {
        rules: [
            {
                test: /\.(?:js|mjs|cjs)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ['@babel/preset-env', {targets: "defaults"}]
                        ]
                    }
                }
            },
            {
                test: /\.scss$/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader",
                ],
            },
        ]
    },
    resolve: {
        extensions: [".css", ".js", ".scss", ".jpg", ".png"],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].bundle.css",
        }),
        new webpack.DefinePlugin({
            "process.env.NOTTOBOARD_WEB_HOST": JSON.stringify(process.env.NOTTOBOARD_WEB_HOST) || JSON.stringify("localhost"),
        }),
        // new CopyPlugin({
        //     patterns: [
        //         { from: "public/img", to: "images" },
        //     ]
        // }),
    ],
    optimization: {
        splitChunks: {
            chunks: "all",
        }
    },
    ignoreWarnings: [
        /public\/sass\/index.scss/
    ]
};