(function(){
window.App = {
    Models: {},
    Collections: {},
    Views: {}
};

window.template = function(id) {
    return _.template( $('#' + id).html() );
};


App.Models.Person = Backbone.Model.extend({
    defaults: {
        name: 'Guest User',
        age: 23,
        occupation: 'Worker',
    },
    validate: function(attrs, options){
        if (attrs.age < 0){
            return 'Age must be positive.';
        }
        if (!attrs.name){
            return 'Everyone must have a name.';
        }
    },
    work: function(){
        return this.get('name') + 'is working.';
    },
});


App.Collections.People = Backbone.Collection.extend({
    model: App.Models.Person,
});


App.Views.People = Backbone.View.extend({
    tagName: 'ul',
    initialize: function(){
        this.collection.on('add', this.addOne, this);
    },
    render: function(){
        this.collection.each(this.addOne, this);
        return this;
    },
    addOne: function(person){
        var personView = new App.Views.Person({model: person});
        this.$el.append(personView.render().el);
    }
});


App.Views.Person = Backbone.View.extend({
    tagName: 'li',
    // className: 'person',
    // id: 'person-id',

    template: template('personTemplate'),

    initialize: function(){
        this.model.on('change', this.render, this);
    },

    events: {
        'click .edit': 'editPerson',
        'click .delete': 'DestroyPerson',
    },

    editPerson: function(){
        var newName = prompt("Please enter the new name", this.model.get('name'));
        this.model.set('name', newName);
    },

    DestroyPerson: function(){
        this.model.destroy();
    },

    remove: function(){
        this.$el.remove();
    },

    render: function(){
        this.$el.html( this.template(this.model.toJSON()));
        return this;
    },
});


App.Views.AddPerson = Backbone.View.extend({
    el: '#addPerson',
    events: {
        'submit': 'submit'
    },
    submit: function(e){
        e.preventDefault();
        var newPersonName = $(e.currentTarget).find('input[type=text]').val();
        var person = new App.Models.Person({name: newPersonName});
        this.collection.add(person);
    }
});


var peopleCollection = new App.Collections.People([
    {
        name: 'Mohit Jain',
        age: 26
    },
    {
        name: 'Taroon Tyagi',
        age: 25,
        occupation: 'web designer'
    },
    {
        name: 'Rahul Narang',
        age: 26,
        occupation: 'Java Developer'
    }
]);

var addPersonView =  new App.Views.AddPerson({collection: peopleCollection});
var peopleView = new App.Views.People({ collection: peopleCollection });
$(document.body).append(peopleView.render().el);
})();
