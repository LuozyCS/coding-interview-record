type book struct {
	key, value int
}

type LRUCache struct {
	capacity  int
	list      *list.List
	keyToNode map[int]*list.Element // int就是page的key
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity:  capacity,
		list:      list.New(),
		keyToNode: make(map[int]*list.Element),
	}

}

func (this *LRUCache) Get(key int) int {
	node := this.keyToNode[key]
	if node == nil {
		return -1
	}
	this.list.MoveToFront(node)
	return node.Value.(book).value // node.Value是给出地址，（book）是类型转换，value才是最后要的值
}

func (this *LRUCache) Put(key int, value int) {
	if node := this.keyToNode[key]; node != nil { // 存在这本书，就用Move
		node.Value = book{key, value}
		this.list.MoveToFront(node)
		return
	}
	this.keyToNode[key] = this.list.PushFront(book{key, value}) // 不存在这本书，就用push
	if len(this.keyToNode) > this.capacity {
		delete(this.keyToNode, this.list.Remove(this.list.Back()).(book).key)
	}
}

// get和put方法的时间复杂度都是O(1)，因此考虑使用双向链表和哈希表实现
// 这个代码是简单版本，复杂版本要像leetcode官方那样实现链表
/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
