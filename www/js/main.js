(function(){
window.App = {
    Models: {},
    Collections: {},
    Views: {},
    Router: {},
};

window.template = function(id) {
    return _.template( $('#' + id).html() );
};


App.Models.Task = Backbone.Model.extend({
    defaults: {
        stage: '1',
        status: '1',
        owner: '1',
    },
    // validate: function(attrs, options){
    //     if (attrs.age < 0){
    //         return 'Age must be positive.';
    //     }
    //     if (!attrs.name){
    //         return 'Everyone must have a name.';
    //     }
    // },
    // work: function(){
    //     return this.get('name') + 'is working.';
    // },
    urlRoot: '/api/tasks/',
});


App.Collections.TaskCollection = Backbone.Collection.extend({
    model: App.Models.Task,
    url: '/api/tasks/',
});


App.Views.TaskCollection = Backbone.View.extend({
    tagName: 'ul',
    initialize: function(){
        this.collection.on('add', this.addOne, this);
    },
    render: function(){
        this.collection.each(this.addOne, this);
        return this;
    },
    addOne: function(task){
        var taskView = new App.Views.Task({model: task});
        this.$el.append(taskView.render().el);
    }
});


App.Views.Task = Backbone.View.extend({
    tagName: 'li',
    // className: 'person',
    // id: 'person-id',

    template: template('taskTemplate'),

    initialize: function(){
        this.model.on('change', this.render, this);
    },

    events: {
        'click .edit': 'editPerson',
        'click .delete': 'DestroyPerson',
    },

    editPerson: function(){
        var newTitle = prompt("Please enter the new title", this.model.get('title'));
        if (newTitle && newTitle!=this.model.get('title')){
            this.model.set('title', newTitle);
            this.model.save();
        }
    },

    DestroyPerson: function(){
        this.model.destroy();
        this.remove();
    },

    remove: function(){
        this.$el.remove();
    },

    render: function(){
        this.$el.html( this.template(this.model.toJSON()));
        return this;
    },
});


App.Views.AddTask = Backbone.View.extend({
    el: '#addTask',
    events: {
        'submit': 'submit'
    },
    submit: function(e){
        e.preventDefault();
        var input = $(e.currentTarget).find('input[type=text]');
        if (input.val().trim()){
            var task = new App.Models.Task({title: input.val()});
            task.save();
            this.collection.add(task);
            input.val('');
        }
    }
});


App.Router = Backbone.Router.extend({
    routes: {
        '': 'index',
        'show/:id': 'show'
    },
    index: function(){
        // $(document.body).append("Index route has ben called..");
    },
    show: function(id){
        // $(document.body).append("Show route has ben called.. with id equals:"+id);
    },
});

var taskCollection = new App.Collections.TaskCollection();
taskCollection.fetch();
new App.Router;
Backbone.history.start();
var addTaskView =  new App.Views.AddTask({collection: taskCollection});
var taskCollectionView = new App.Views.TaskCollection({ collection: taskCollection });
$(document.body).append(taskCollectionView.render().el);
})();
