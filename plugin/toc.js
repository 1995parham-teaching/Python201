/*
 * +===============================================
 * | Author:        Parham Alvani (parham.alvani@gmail.com)
 * |
 * | Creation Date: 03-08-2017
 * |
 * | File Name:     toc.js
 * +===============================================
 */
const toc = {
  initToCOnLoad: function (titles) {
    let sections = document.getElementsByClassName('toc')
    for (let section of sections) {
      const titlesListElement = document.createElement('ul');

      for (let title of titles) {
        let node = document.createElement('li');
        node.appendChild(document.createTextNode(title));
        titlesListElement.appendChild(node);
      }

      if (section.dataset.selected) {
        for (let i = 0; i < titlesListElement.children.length; i++) {
          if (titlesListElement.children[i].innerText === section.dataset.selected) {
            titlesListElement.children[i].className += 'material-select'
          }
        }
      }
      section.appendChild(titlesListElement);
    }
  }
}
