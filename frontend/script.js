const API_URL = "http://127.0.0.1:5000/find_players";  // Flask 서버 주소

async function findPlayers() {
    const position = document.getElementById("position").value;
    const height = document.getElementById("height").value;
    const resultList = document.getElementById("result");
    resultList.innerHTML = "";  // 결과 초기화

    if (!position || !height) {
        alert("포지션과 키를 입력하세요.");
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ position, height })
        });

        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }

        // 결과 표시
        data.similar_players.forEach(player => {
            const li = document.createElement("li");
            li.textContent = player;
            resultList.appendChild(li);
        });

    } catch (error) {
        console.error("Error:", error);
        alert("서버 요청에 실패했습니다.");
    }
}
