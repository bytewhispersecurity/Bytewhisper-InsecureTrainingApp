import { sqliteTable, text, integer, uniqueIndex } from 'drizzle-orm/sqlite-core';

export const user = sqliteTable('user', {
	id: integer('id').primaryKey({ autoIncrement: true}),
	firstName: text('first_name'),
	lastName: text('last_name'),
	email: text().notNull(),
	age: integer('age'),
	ssn: integer('ssn'),
	address: text('address'),
	},
	(sqliteTable) => {
		uniqueIndex("email_idx").on(sqliteTable.email)
	}
);

export const posts = sqliteTable('posts', {
	id: integer().primaryKey({ autoIncrement: true}),
	slug: text().$default(() => generateUniqueString(16)),
	title: text(),
	ownerId: integer('').references(() => user.id),
})

export const comments = sqliteTable('comments', {
	id: integer().primaryKey({ autoIncrement: true }),
	text: text({ length: 256 }),
	postId: integer('post_id').references(() => posts.id),
	ownerId: integer('owner_id').references(() => user.id),
})

function generateUniqueString(length: number = 12): string {
	const characters =
	  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
	let uniqueString = "";
	for (let i = 0; i < length; i++) {
	  const randomIndex = Math.floor(Math.random() * characters.length);
	  uniqueString += characters[randomIndex];
	}
	return uniqueString;
  }