const { response } = require("express");
const express = require("express");
const bodyParser = require("body-parser");

const http = require("http");

const axios = require('axios')

const app = express();
app.set('view engine', 'ejs');
app.use(express.static("public"));

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", function (req, res) {

    const url = "http://15.207.18.80:8081/memes/";
    http.get(url, function (response) {
        response.on("data", function (data) {
            const memeContent = JSON.parse(data);
            console.log(memeContent.length)
            res.render("display", {
                startingContent: memeContent,
            });
        });
    });


});

app.post("/", function (req, res) {
    const url = "http://15.207.18.80:8081/memes/";

    const memeData = JSON.stringify({
        name: req.body.name,
        caption: req.body.caption,
        url: req.body.url
    });
    console.log(memeData);

    axios
        .post(url, memeData)
        .then(res => {
            console.log(`statusCode: ${res.statusCode}`)
            console.log(res)
        })
        .catch(error => {
            console.error(error)
        });

    res.redirect('/');

});

app.post("/memes/:memeid", function (req, res) {
    const reqMemeId = req.params.memeid;

    const url = "http://15.207.18.80:8081/memes/" + reqMemeId;
    const memeData = JSON.stringify({
        'caption': req.body.edit_caption,
        'url': req.body.edit_url
    });

    console.log(url)
    console.log(memeData)

    axios
        .patch(url, memeData)
        .then(res => {
            console.log(`statusCode: ${res.statusCode}`)
            console.log(res)
        })
        .catch(error => {
            console.error(error)
        });

    res.redirect("/")
})

app.listen(3000, function () {
    console.log("Server at 3000");
})