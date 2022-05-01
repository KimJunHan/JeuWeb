var id = "";
var pw = "";

var user_id = prompt("아이디를 입력해주세요.");
var user_pasword = prompt("비밀번호를 입력해주세요.");

if(id == user_id)
{
    if (pw==user_pasword) {
        location.href = "../templates/html/main.html"
    }
    else {
        document.write("비밀번호가 일치하지 않습니다.");
        location.reload();
    }
}
else {
    document.write("아이디가 일치하지 않습니다.");
    location.reload();
}