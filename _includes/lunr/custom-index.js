const content_to_merge = [docs[i].content, docs[i].mtorg_alt_names];
docs[i].content = content_to_merge.join(' ');
