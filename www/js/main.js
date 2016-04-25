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
    },
    validate: function(attrs, options){
    },
    urlRoot: '/api/tasks/',
});


App.Collections.TaskSet = Backbone.Collection.extend({
    model: App.Models.Task,
    url: '/api/tasks/',
});


App.Views.TaskSet = Backbone.View.extend({
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

    template: template('item-Template'),

    events: {
        // 'click .toggle': 'toggleCompleted',
        // 'dblclick label': 'edit',
        // 'click .destroy': 'clear',
        // 'keypress .edit': 'updateOnEnter',
        // 'keydown .edit': 'revertOnEscape',
        // 'blur .edit': 'close'
    },

    initialize: function(){
        this.model.on('change', this.render, this);
    },

    // events: {
    //     'click .edit': 'editPerson',
    //     'click .delete': 'DestroyPerson',
    // },

    // editPerson: function(){
    //     var newName = prompt("Please enter the new name", this.model.get('name'));
    //     this.model.set('name', newName);
    // },

    // DestroyPerson: function(){
    //     this.model.destroy();
    // },

    // remove: function(){
    //     this.$el.remove();
    // },

    render: function(){
        this.$el.html( this.template(this.model.toJSON()));
        return this;
    },
});


// App.Views.AddPerson = Backbone.View.extend({
//     el: '#addPerson',
//     events: {
//         'submit': 'submit'
//     },
//     submit: function(e){
//         e.preventDefault();
//         var newPersonName = $(e.currentTarget).find('input[type=text]').val();
//         var person = new App.Models.Person({name: newPersonName});
//         this.collection.add(person);
//     }
// });


App.Router = Backbone.Router.extend({
    routes: {
        '': 'index',
        'task/:id': 'task'
    },
    index: function(){
        $(document.body).append("Index route has ben called..");
    },
    task: function(id){
        $(document.body).append("Task route has ben called.. with id equals:"+id);
    },
});

// var peopleCollection = new App.Collections.People([
//     {
//         name: 'Mohit Jain',
//         age: 26
//     },
//     {
//         name: 'Taroon Tyagi',
//         age: 25,
//         occupation: 'web designer'
//     },
//     {
//         name: 'Rahul Narang',
//         age: 26,
//         occupation: 'Java Developer'
//     }
// ]);

// var oldSync = Backbone.sync;
// Backbone.sync = function(method, model, options){
//   options.beforeSend = function(xhr){
//     xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
//   };
//   return oldSync(method, model, options);
// };

new App.Router;
Backbone.history.start();
// $(document.body).append(peopleView.render().el);
})();
