function copyToClipboard(btn, text) {
  navigator.clipboard.writeText(text).then(() => {
    btn.classList.add("copied");
    btn.innerText = "Copied";
    setTimeout(() => {
      btn.classList.remove("copied");
      btn.innerText = "Copy";
    }, 2000);
  });
}
function showOnlyExperience() {
  document.querySelectorAll(".tl-item.education").forEach((div) => {
    div.style.display = "none";
  });
  document.querySelectorAll(".tl-item.experience").forEach((div) => {
    div.style.display = "grid";
  });
  document.getElementById("ExperienceButton").classList.add("btn-primary");
  document.getElementById("ExperienceButton").classList.remove("btn-ghost");
  document.getElementById("EducationButton").classList.add("btn-ghost");
  document.getElementById("EducationButton").classList.remove("btn-primary");
  document.getElementById("AllButton").classList.add("btn-ghost");
  document.getElementById("AllButton").classList.remove("btn-primary");
}
function showOnlyEducation() {
  document.querySelectorAll(".tl-item.experience").forEach((div) => {
    div.style.display = "none";
  });
  document.querySelectorAll(".tl-item.education").forEach((div) => {
    div.style.display = "grid";
  });
  document.getElementById("ExperienceButton").classList.add("btn-ghost");
  document.getElementById("ExperienceButton").classList.remove("btn-primary");
  document.getElementById("EducationButton").classList.add("btn-primary");
  document.getElementById("EducationButton").classList.remove("btn-ghost");
  document.getElementById("AllButton").classList.add("btn-ghost");
  document.getElementById("AllButton").classList.remove("btn-primary");
}
function showBoth() {
  document.querySelectorAll(".tl-item.education").forEach((div) => {
    div.style.display = "grid";
  });
  document.querySelectorAll(".tl-item.experience").forEach((div) => {
    div.style.display = "grid";
  });
  document.getElementById("ExperienceButton").classList.add("btn-ghost");
  document.getElementById("ExperienceButton").classList.remove("btn-primary");
  document.getElementById("EducationButton").classList.add("btn-ghost");
  document.getElementById("EducationButton").classList.remove("btn-primary");
  document.getElementById("AllButton").classList.add("btn-primary");
  document.getElementById("AllButton").classList.remove("btn-ghost");
}
