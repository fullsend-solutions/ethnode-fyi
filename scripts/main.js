
// Shortcuts to DOM Elements.
var recentPostsSection = document.getElementById('recent-posts-list');
var listeningFirebaseRefs = [];

function createLineElement(dataKey, line) {
  var html =
      '<div class="post post-' + dataKey + '">' +
      '<div class="text"></div>' +
      '</div>';

  // Create the DOM element from the HTML.
  var div = document.createElement('div');
  div.innerHTML = html;
  var postElement = div.firstChild;

  // Set values.
  postElement.getElementsByClassName('text')[0].innerText = line;

  return postElement;
}

/**
 * Starts listening for new lines and populates line list.
 */
function startDatabaseQueries() {
  var recentPostsRef = firebase.database().ref('lines').limitToLast(100);

  var fetchPosts = function(postsRef, sectionElement) {
    postsRef.on('child_added', function(data) {
      var containerElement = sectionElement.getElementsByClassName('posts-container')[0];
      containerElement.insertBefore(
          createLineElement(data.key, data.val().line),
         containerElement.firstChild);
    });
  };

  fetchPosts(recentPostsRef, recentPostsSection);
  listeningFirebaseRefs.push(recentPostsRef);
}

window.addEventListener('load', function() {
  startDatabaseQueries();
}, false)