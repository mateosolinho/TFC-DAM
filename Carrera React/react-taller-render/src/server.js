const express = require('express');

const app = express();

app.use(express.static('public'))

app.use('*', require('../dist/ssr.js'));

app.listen(8080, () => {
    console.log('Servers running on 8080 port')
})