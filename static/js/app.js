$(document).ready(function () {
  function checkVisibility() {
    let windowHeight = $(window).height(); // 視窗高度
    let scrollY = $(window).scrollTop(); // 滾動位置

    $(".fadeInScroll").each(function () {
      let position = $(this).offset().top; // 獲取元素頂部相對於文檔頂部的位置
      let elementBottom = position + $(this).outerHeight(); // 獲取元素底部的位置

      // 检查元素是否進入是視窗
      if (scrollY + windowHeight >= position && scrollY <= elementBottom) {
        $(this).addClass("active");
      } else {
        $(this).removeClass("active"); // 移除 'active' 以重置
      }
    });
  }

  //绑定滾動事件;
  $(window).scroll(checkVisibility);
  checkVisibility(); // 初始检查
});

$(document).ready(function () {
  setInterval(function () {
    let topBackground = $(".background-image");
    let currentImage = topBackground.css("background-image");

    if (currentImage.includes("image2.jpg")) {
      topBackground.css(
        "background-image",
        'url("../static/upload/image1.jpg")'
      );
    } else if (currentImage.includes("image1.jpg")) {
      topBackground.css(
        "background-image",
        'url("../static/upload/image3.jpg")'
      );
    } else {
      topBackground.css(
        "background-image",
        'url("../static/upload/image2.jpg")'
      );
    }
  }, 3000);
});
