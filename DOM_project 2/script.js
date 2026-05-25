document.addEventListener('DOMContentLoaded', function () {
  let colorBox = document.getElementById('color-box');
  let changeColorBtn = document.getElementById('change-color-btn');

  function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  changeColorBtn.addEventListener('click', function () {
    colorBox.style.backgroundColor = getRandomColor();
  });
});
