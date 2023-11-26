db.createUser({
    user: 'appuser',
    pwd: 'appuserpassword',
    roles: [
      {
        role: 'readWrite',
        db: 'userDB',
      },
    ],
  });
  
  db.createCollection('users');