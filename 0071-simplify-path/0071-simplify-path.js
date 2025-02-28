var simplifyPath = function(path) {
    // Split the path by slashes
    const components = path.split('/');
    // Stack to store the valid directory names
    let stack = [];

    for (let component of components) {
        if (component === '' || component === '.') {
            // Ignore empty or '.' components
            continue;
        }
        if (component === '..') {
            // '..' means go up one level (pop the last directory from stack)
            if (stack.length > 0) {
                stack.pop();
            }
        } else {
            // Otherwise, it's a valid directory name, add it to the stack
            stack.push(component);
        }
    }

    // Join the stack to form the canonical path
    return '/' + stack.join('/');
};
