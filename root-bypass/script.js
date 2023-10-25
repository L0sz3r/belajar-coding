Java.perform(function() {
    Java.use("sg.vantagepoint.uncrackable1.MainActivity").a.implementation = function(s) {
        console.log("Tamper Detection, Message Was : " + s);
    }
});
