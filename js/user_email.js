var userEmail = prompt("당신의 메일 주소는?");
var arrUrl = [".co.kr", ".com", ".net", ".or.kr", "go.kr"];

var checkEmail1 = false;
var checkEmail2 = false;

if(userEmail.indexOf("@")>0) {
    checkEmail1 = true;
}

for(var i = 0; i < arrUrl.length; i++)
{
    if(userEmail.indexOf(arrUrl[i] > 0))
    {
        checkEmail2=true;
    }
}

if(checkEmail1 && checkEmail2)
{
    document.write(userEmail);
}
else{
    alert("입력하신 이메일 형식이 잘못됐습니다.")
}