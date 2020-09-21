$(document).ready(function(){
    setTimeout(function () {
      $("#cookieConsent").fadeIn(200);
    }, 3000);
    $("#closeCookieConsent").click(function() {
      $("#cookieConsent").fadeOut(200);
    });
    $(".cookieConsentOK").click(function() {
       var expTime = (new Date(Date.now() + 365 * 86400 * 1000)).toUTCString(); // 1 year from now
       document.cookie = "accept_cookies=True; expires=" + expTime + ";path=/";
       $("#cookieConsent").fadeOut(200);
    });
});
