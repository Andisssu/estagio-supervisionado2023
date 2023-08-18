const dropdown = document.querySelector('.dropdown');
const dropdownContent = document.querySelector('.dropdown-content');

dropdown.addEventListener('mouseover', () => {
  dropdownContent.style.display = 'block';
});

dropdown.addEventListener('mouseout', () => {
  dropdownContent.style.display = 'none';
});
